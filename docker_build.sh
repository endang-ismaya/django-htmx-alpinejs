#!/bin/zsh

# Update requirements.txt
pip freeze > requirements.txt

# image var
IMAGE_NAME=ude_jose


# Function to increment the version
increment_version() {
  local current_version="$1"
  local major minor patch

  # Extract major, minor, and patch numbers
  IFS='.' read -r major minor patch <<< "${current_version}"

  patch=$((patch + 1))

  if [[ $patch -gt 9 ]]; then
    patch=0
    minor=$((minor + 1))
    if [[ $minor -gt 9 ]]; then
      minor=0
      major=$((major + 1))
    fi
  fi

  echo "$major.$minor.$patch"
}

# Get the latest existing version
latest_version=$(docker images --format "{{.Tag}}" $IMAGE_NAME | grep -o 'v[0-9]\+\.[0-9]\+\.[0-9]\+' | sort -V | tail -n 1)

if [[ -z "$latest_version" ]]; then
  # No existing image, start with v0.0.1
  new_version="v0.0.1"

  # Build the image with the new version tag
  docker build -t "$IMAGE_NAME:$new_version" .

  echo "Built image: $IMAGE_NAME:$new_version"

  # show images
  docker images

else
  # Extract the version number (remove the "ude_jose:" prefix)
  version_number="${latest_version#v}"

  # Increment the version
  new_version="v$(increment_version "$version_number")"

  # delete existing
  # delete previous containers
  docker stop "$IMAGE_NAME"
  docker rm "$IMAGE_NAME"
  docker rmi "$IMAGE_NAME:$latest_version"

  # Build the image with the new version tag
  docker build -t "$IMAGE_NAME:$new_version" .

  echo "Built image: $IMAGE_NAME:$new_version"

  # show images
  docker images

fi


# create the container
docker run -d -p 8000:8000 --name "$IMAGE_NAME" -e TARGET_CONTAINER=$IMAGE_NAME -v $(pwd):/app "$IMAGE_NAME:$new_version"

echo "Container $IMAGE_NAME has been created."

# list docker
docker ps
