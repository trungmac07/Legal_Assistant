FROM node:18

WORKDIR /usr/src/app

# Copy package files
COPY package*.json ./

# Clean npm cache and install with verbose output
RUN npm cache clean --force && \
    npm ci --no-audit --no-fund --verbose

COPY . .

EXPOSE 3000

CMD ["npm", "start", "--", "--host", "0.0.0.0"]