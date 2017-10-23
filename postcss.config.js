module.exports = ({ env }) => ({
    plugins: {
        "autoprefixer": env === "production" ? true : false
    }
});
