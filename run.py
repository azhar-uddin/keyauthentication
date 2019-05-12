from app import create_app

app = create_app(None)

@app.context_processor
def inject_variables():
    return dict(envrionment=app.config.get('ENV', 'ENV'), app_name=app.config.get('APP_NAME', 'APP_NAME'))

if __name__ == '__main__':
    app.run()

@app.shell_context_processor
def make_shell_context():
    return {
    	'app': app
    	}