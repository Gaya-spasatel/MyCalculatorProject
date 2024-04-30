FROM php:7.4-apache

RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

RUN echo "ServerName calculatorclient" >> /etc/apache2/apache2.conf
COPY src/ /var/www/html/