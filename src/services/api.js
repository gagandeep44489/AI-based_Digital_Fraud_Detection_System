import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 10000,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export async function createMessage(payload) {
  const { data } = await api.post("/messages", payload);
  return data;
}

export async function fetchPrediction(messageId) {
  const { data } = await api.get(`/predictions/${messageId}`);
  return data;
}

export default api;
