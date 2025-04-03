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
latest_version=$(docker images --format "{{.Tag}}" ude_jose | grep -o 'v[0-9]\+\.[0-9]\+\.[0-9]\+' | sort -V | tail -n 1)

if [[ -z "$latest_version" ]]; then
  # No existing image, start with v0.0.1
  new_version="v0.0.1"
else
  # Extract the version number (remove the "ude_jose:" prefix)
  version_number="${latest_version#v}"

  # Increment the version
  new_version="v$(increment_version "$version_number")"
fi

# Build the image with the new version tag
docker build -t "ude_jose:$new_version" .

echo "Built image: ude_jose:$new_version"

# show images
docker images