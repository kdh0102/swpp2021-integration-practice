module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
    jest: true, // This is for jest
  },
  extends: ["plugin:react/recommended", "airbnb"],
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 13,
    sourceType: "module",
  },
  plugins: ["react"],
  rules: {},
};
