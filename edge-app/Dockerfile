# Create image based on the official Node 6 image from dockerhub
FROM node:6


ENV APP_ROOT /edge-app

# Create a directory where our app will be placed
RUN mkdir -p $APP_ROOT

# Change directory so that our commands run inside this new directory
WORKDIR $APP_ROOT

# Copy dependency definitions
COPY package.json $APP_ROOT

# Install dependecies
RUN npm install

# Get all the code needed to run the app
COPY . $APP_ROOT

# Expose the port the app runs in
EXPOSE 4200

# Serve the app
CMD ["npm", "start"]
