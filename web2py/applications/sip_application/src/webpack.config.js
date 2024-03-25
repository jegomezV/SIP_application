const path = require('path');

module.exports = {
  mode: 'development',
  entry: './Students.ts', // El punto de entrada de tu aplicación
  output: {
    path: path.resolve("webpack", 'js'), // La ruta donde se colocarán los archivos transpilados
    filename: 'students.js', // El nombre del archivo de salida
  },
  resolve: {
    extensions: ['.ts', '.js'], // Las extensiones de archivo que Webpack debería manejar
  },
  module: {
    rules: [
      {
        test: /\.ts$/, // Todos los archivos .ts
        use: 'ts-loader', // Usar ts-loader para transpilar TypeScript a JavaScript
        exclude: /node_modules/, // Excluir la carpeta node_modules
      },
    ],
  },
};