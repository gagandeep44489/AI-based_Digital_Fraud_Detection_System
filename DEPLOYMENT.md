# Deployment Guide (FastAPI + React)

This guide covers beginner-friendly deployment on **Render** and **AWS EC2** with optional Docker.

---

## 1) Render Deployment

### A. Backend (FastAPI) on Render Web Service

#### Files used
- `Procfile`
- `runtime.txt`
- `requirements.txt`

#### Steps
1. Push this repository to GitHub.
2. In Render dashboard, click **New +** → **Web Service**.
3. Connect your repo.
4. Configure:
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
5. Add environment variables in Render:
   - `DATABASE_URL=...`
   - `SECRET_KEY=...`
6. Deploy and verify:
   - Open `https://<your-backend>.onrender.com/docs`

### B. Frontend (React) on Render Static Site

1. In Render dashboard, click **New +** → **Static Site**.
2. Connect the same repo.
3. Configure:
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `dist`
4. Add frontend env var:
   - `VITE_API_BASE_URL=https://<your-backend>.onrender.com`
5. Deploy.

> Alternative: Use Vercel for frontend with same build command and `dist` output.

---

## 2) AWS EC2 Deployment (Ubuntu)

## A. Launch and connect
1. Launch Ubuntu EC2 (22.04+).
2. Open security group ports:
   - `22` (SSH)
   - `80` (HTTP)
   - `443` (HTTPS, optional)
3. SSH into server:
```bash
ssh -i /path/to/key.pem ubuntu@<EC2_PUBLIC_IP>
```

## B. Install system packages
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git nginx curl
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

## C. Clone project
```bash
git clone <YOUR_REPO_URL>
cd AI-based_Digital_Fraud_Detection_System
```

## D. Backend setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set:
- `DATABASE_URL`
- `SECRET_KEY`

Run backend:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

(Optional production process manager):
```bash
pip install gunicorn
gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:10000
```

## E. Frontend setup
```bash
npm install
VITE_API_BASE_URL=http://<EC2_PUBLIC_IP>/api npm run build
```

Copy build files:
```bash
sudo mkdir -p /var/www/fraud-frontend
sudo cp -r dist /var/www/fraud-frontend/
```

## F. Nginx reverse proxy
1. Copy provided config:
```bash
sudo cp nginx.conf /etc/nginx/sites-available/fraud-detection
```
2. Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/fraud-detection /etc/nginx/sites-enabled/fraud-detection
sudo rm -f /etc/nginx/sites-enabled/default
```
3. Test and reload:
```bash
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl enable nginx
```

Now:
- Frontend: `http://<EC2_PUBLIC_IP>`
- API via Nginx: `http://<EC2_PUBLIC_IP>/api/...`

---

## 3) Optional Docker Deployment (Backend)

Build image:
```bash
docker build -t fraud-backend .
```

Run container:
```bash
docker run -d --name fraud-backend \
  -p 10000:10000 \
  --env-file .env \
  fraud-backend
```

Check logs:
```bash
docker logs -f fraud-backend
```

---

## 4) Required Environment Variables

Minimum values:
- `DATABASE_URL`
- `SECRET_KEY`

Frontend:
- `VITE_API_BASE_URL`

