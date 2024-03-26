const glob = require('glob');
const path = require('path');

module.exports = {
  mode: 'development',
  devtool: 'source-map',
  entry: path.resolve(__dirname, './renderer/Students.ts'), // Cambia esta línea
  output: {
    path: path.resolve(__dirname, '../dist'), // Cambia esta línea
    filename: '[name].js', // Cambia esta línea
    library: '[name]', // Cambia esta línea
    libraryTarget: 'umd',
  },
  resolve: {
    extensions: ['.ts', '.js'],
  },
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
};
