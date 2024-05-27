import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

// Interceptor to add the token to request headers
api.interceptors.request.use(
  // Success
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN); // Retrieve AccessToken
    if (token) {
      config.headers.Authorization = `Bearer ${token}`; // Add to headers
    }
    return config;
  },
  // Error
  (error) => {
    console.log("ERROR");
    return Promise.reject(error);
  }
);

export default api;
