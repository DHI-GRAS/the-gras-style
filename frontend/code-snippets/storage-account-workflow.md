# Github actions workflow for Storage Account deployment

```
name: Azure storage account CI

on:
  push:
    branches: [ main ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Node.js version
	uses: actions/setup-node@v2
	with:
	  node-version: '14'

      - name: Install dependencies
        run: yarn install

      - name: Build
	run: yarn build

      # Deploys the app on a storage account in the $web container.
      # The connection string can be found in the Access Keys menu item from the created storage account. 
      # Copy it and store it in secrets.
      
      - name: Azure Blob Upload
        uses: LanceMcCarthy/Action-AzureBlobUpload@v1.9.0
        with:
          source_folder: "build"
          container_name: "$web"
          connection_string: ${{ secrets.BlobConnectionString }}
          clean_destination_folder: true
          destination_folder: ./
```

More details about this action can be found in the [https://github.com/LanceMcCarthy/Action-AzureBlobUpload](https://github.com/LanceMcCarthy/Action-AzureBlobUpload#readme)
