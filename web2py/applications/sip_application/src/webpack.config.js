const path = require('path');

module.exports = {
  mode: 'development',
  devtool: 'source-map',
  entry: './repository/StudentRepository.ts',
  output: {
    path: path.resolve("webpack", 'js'),
    filename: 'StudentRepository.js',
    library: 'StudentRepository',
    libraryTarget: 'umd', // Cambia esta línea
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
