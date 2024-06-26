# Respiratory Disease: Tapyr Version

This repository contains the tapyr migration of [the pure PyShiny Respiratory Disease dashboard](https://github.com/Appsilon/respiratory_disease_pyshiny), which originates from the R/Shiny version [Respiratory Disease app](https://connect.appsilon.com/respiratory_disease_app_sprint/).

## Explore the app
The app is deployed at [Appsilon Posit Connect](https://connect.appsilon.com/respiratory-disease-tapyr/).

## How to run

(This section is copied from the tapyr template)

### Using Devcontainer

To ensure a consistent development experience across all environments, we recommend using the [devcontainer](https://code.visualstudio.com/docs/remote/containers) configuration with Visual Studio Code or DevPod for container-based development.

1. **Start the Devcontainer**: Open the project in VS Code and select "Reopen in Container" when prompted, or use the Command Palette (`Ctrl+Shift+P`) and choose "Remote-Containers: Reopen in Container". Alternatively, use [DevPod](https://devpod.sh/) following their instructions.
2. **Activate the virtual environment**:
   ```sh
   poetry shell
   ```
3. **Run the application**:
   ```sh
   shiny run app.py --reload
   ```
4. **Execute tests**:
   ```sh
   poetry run pytest
   ```

*Note*: The Devcontainer might limit some `playwright` features, such as `codegen`. For full functionality, consider a local setup.

### Setting Up Locally with Poetry

For developers preferring a local setup without Devcontainer:

1. **Install pipx**: Ensure pipx is installed for managing isolated CLI apps.
2. **Install Poetry**:
   ```sh
   pipx install poetry
   ```
3. **Clone the repository** and navigate to it.
4. **Install dependencies**:
   ```sh
   poetry install
   playwright install
   ```

*Attention*: Follow any additional steps prompted by `playwright install`.

### Deployment on Posit Connect

Deploy your application to Posit Connect by:

1. **Exporting your API Key**:
   ```sh
   export CONNECT_API_KEY="your_api_key_here"
   ```
2. **Configuring Posit Connect**:
   ```sh
   rsconnect add \
   --api-key $CONNECT_API_KEY \
   --server <MY_CONNECT_URL> \
   --name <SERVER_NAME>
   ```
3. **Deploying**:
   ```sh
   rsconnect deploy shiny -t "Tapyr App" .
   ```

Replace placeholders with your server URL, server name, and API key. Verify the deployment on Posit Connect for successful upload.

---

Developed with :heart: at [Appsilon](https://appsilon.com).
Get in touch: <opensource@appsilon.com>.

Want to stay up to date with Tapyr and other packages? Join 4,2k explorers and get the [📧 Shiny Weekly Newsletter](https://go.appsilon.com/shiny-weekly?utm_source=community&utm_medium=github&utm_content=tapyr) into your mailbox and check our [Slack community](https://go.appsilon.com/shiny4allcommunity).

Explore the [Rhinoverse](https://rhinoverse.dev) - a family of R packages built around [Rhino](https://appsilon.github.io/rhino/)!

Appsilon is a
[**Posit (formerly RStudio) Full Service Certified Partner**](https://www.rstudio.com/certified-partners/).

<a href="https://appsilon.com/careers/">
  <img src="https://raw.githubusercontent.com/Appsilon/website-cdn/gh-pages/WeAreHiring1.png" alt="We are hiring!">
</a>
