# Utiliser l'image originale comme base
FROM ghcr.io/stephengpope/no-code-architects-toolkit:main

# Copier le fichier s3_toolkit modifié
COPY s3_toolkit_fixed.py /app/services/s3_toolkit.py
