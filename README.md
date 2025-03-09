# SPS Validator Playground
A Swagger UI playground for interacting with SPS Validator APIs.

## Introduction
This repository provides a Docker container that serves a Swagger UI playground for experimenting with the SPS Validator API.

The OpenAPI specification is based on the official spec found here:
🔗 [SPS Validator OpenAPI Spec](https://github.com/TheSPSDAO/SPS-Validator/blob/master/apps/sps-validator-ui/openapi.yaml)

Additionally, I have added missing API calls that are available in the code but were not included in the official OpenAPI spec.

If anything is missing or not working, feel free to open an issue or reach out!

##  How It Works
This container fetches the top 10 active validators from: 🔗 https://thespsdao.github.io/SPS-Validator/validators?limit=10&active=true <br>
It dynamically updates the OpenAPI spec with the validator APIs.<br>
Runs Swagger UI to explore and test the APIs.<br>
Includes extra API endpoints that were missing from the official OpenAPI file.<br>

## 🚀 Run Locally
Using the Latest Version
```
docker pull gamerbeaker/splinterlands-validator-swagger:latest
docker run -p 8080:8080 gamerbeaker/splinterlands-validator-swagger:latest
```
Using a Specific Version
```
docker pull gamerbeaker/splinterlands-validator-swagger:v1.0.0
docker run -p 8080:8080 gamerbeaker/splinterlands-validator-swagger:v1.0.0
```

Once running, open your browser and navigate to:
🔗 http://localhost:8080

You will see the Swagger UI with the dynamically updated OpenAPI spec!

# Missing or Incorrect Endpoints?
If you find any issues, incorrect responses, or missing endpoints, feel free to:<br>
📌 Open an issue<br>
📌 Submit a pull request<br>
📌 Reach out to me directly<br>

## Contributing
Contributions are welcome! If you’d like to add new features or improve existing functionality, feel free to fork the repo and submit a pull request.

## License

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.
