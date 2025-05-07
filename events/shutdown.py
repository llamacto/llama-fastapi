from fastapi import FastAPI


def shutdown_event(app: FastAPI):
    @app.on_event("shutdown")
    async def shutdown():
        # Add any cleanup code here
        pass 