FROM nginx:alpine

# Copier le fichier de configuration nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copier les certificats SSL
COPY your_certificate.crt /etc/ssl/certs/your_certificate.crt
COPY your_certificate.key /etc/ssl/private/your_certificate.key
