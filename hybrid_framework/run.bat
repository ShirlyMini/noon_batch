pytest -v -s -m "regression" --html=.\Repots\log_regression.html --browser=edge
 rem -n=2
rem pytest -v -s -m "sanity" --html=.\Repots\log_sanit.html --browser=edge -n=2
pytest -v -s -m "sanity" --html=.\Repots\log_regression.html --browser=chrome
 rem -n=2