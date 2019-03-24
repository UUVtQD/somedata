FROM python:3.7-alpine
LABEL author="Sergii Kotenko"
ADD getweather.py /
RUN pip install pyowm
CMD ["python", "/getweather.py"]
