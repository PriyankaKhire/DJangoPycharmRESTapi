# DJangoPycharmRESTapi
Creating REST api using Django and PyCharm

## Errors Faced
```
Could not find platform independent libraries
```
[Delete all python installations](https://stackoverflow.com/questions/3515673/how-to-completely-remove-python-from-a-windows-machine)

remove python from environment variables -> Start -> Type "Environment Variables"
![Screenshot 2024-03-30 220024](https://github.com/PriyankaKhire/DJangoPycharmRESTapi/assets/12015512/9d57947f-7b68-47f5-a808-63aaa122826b)
![2](https://github.com/PriyankaKhire/DJangoPycharmRESTapi/assets/12015512/4f69913e-104b-4aa2-8ef5-ea3435796693)
![3](https://github.com/PriyankaKhire/DJangoPycharmRESTapi/assets/12015512/f429e26d-6bae-42fd-8111-7fcad209c453)

Finally start PyCharm and install python through it.

Note: always install poetry inside virtual environment using terminal commands. Do not try to install it via Pycharm


## Film app
- [ReadMe.md](film_app_django/README.md)
- This project has 2 simple APIs
  - GET
  - POST
![Screenshot 2024-02-22 174841](https://github.com/PriyankaKhire/DJangoPycharmRESTapi/assets/12015512/f0b96ce9-9a3d-48fc-81d6-ca01637af3bc)

## To Read CSV file
- [ReadMe.md](ReadCsv/README.md)
- This project reads the contents of a CSV file into the DB

## To read CSV and REST api to GET
- [ReadMe.md](ReadCsvAndGET/README.md)
- This project reads the contents of CSV file and has 1 API
  - GET: Display contents of the CSV

## Intuit Interview
- In this project we Read contents of CSV file and display using GET api

