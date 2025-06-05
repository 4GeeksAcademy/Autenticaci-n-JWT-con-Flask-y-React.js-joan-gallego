from src.api import create_app

app = create_app()

if __name__ == '__main__':
    # Corre en el puerto 3001 como dices
    app.run(host='0.0.0.0', port=3001, debug=True)
