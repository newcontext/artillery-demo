## How to use Artillery


### Install artillery

```
npm install -g artillery
```


### Run the examples

```
artillery run example1.yml
```


#### Brief description of examples

* example1.yml: simple GET
* example2.yml: POST request with JSON data
* example3.yml: capturing data from previous requests
* example4.yml: using a JS processor to avoid hardcoding data
* example5.yml: traffic phases and flows, flow naming and weights


### Notes

The simple API code is included.

All the API users are stored in `users.json`, a pre-generated file to act in lieu of a database for simplicity sake.

