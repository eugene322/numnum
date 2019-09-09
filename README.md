### Seed

#### For development:
``` $ find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs sudo rm -rf ```

``` $ chmod +x src/entrypoint.sh ```

``` $ docker-compose up ```

### Run tests:
In separate tab

``` $ docker-compose exec django bash ``` - get into django container

``` $ pytest -v --cov . --cov-report term-missing --cov-fail-under 100 \ ```

``` --flake8 -n 4 --no-migrations --reuse-db ``` - run all tests
