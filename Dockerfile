# Use the official Nginx image as the base image
FROM nginx:alpine

# Copy the static files from your project to the Nginx html directory
COPY . /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
