module.exports = ({ options, env }) => ({
    plugins: {
        "autoprefixer": env === "production" ? options.autoprefixer : false
    }
});
