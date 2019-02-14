FROM rcourt/loadedubuntu

COPY checkImageFiles.py /checkImageFiles.py

ENTRYPOINT ["python", "checkImageFiles.py"]

