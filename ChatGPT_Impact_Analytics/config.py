class Config:
    DEBUG = True
    # Add other configuration variables if needed

# Load configuration
def load_config(app):
    app.config.from_object(Config)
