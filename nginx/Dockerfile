FROM nginx:1.27.3

RUN rm /etc/nginx/conf.d/default.conf \
    && rm /usr/share/nginx/html/index.html \
    && chmod -R 755 /usr/share/nginx/html/

COPY nginx/project.conf /etc/nginx/conf.d/
COPY nginx/index.html /usr/share/nginx/html
