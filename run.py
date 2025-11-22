import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
        reload_dirs=["app"],
        host="localhost",
        port=8000,
        ssl_keyfile="app/certs/key.pem",
        ssl_certfile="app/certs/cert.pem"
    )
    print("Running CampusAI API...")    