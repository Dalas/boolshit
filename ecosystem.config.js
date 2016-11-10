module.exports = {
  /**
   * Application configuration section
   * http://pm2.keymetrics.io/docs/usage/application-declaration/
   */
  apps : [

    // First application
    {
      name      : "course-project",
      script    : "./main.py",
      interpreter: "python3",
      "post_update": ["./builder.sh"],
      "env_webhook": {
        "port": "8889",
        "path": "/webhook",
        "secret": "KHNUofRE",
        "pre_hook": "",
        "post_hook": ""
      }
    }
  ],

  /**
   * Deployment section
   * http://pm2.keymetrics.io/docs/usage/deployment/
   */
  deploy : {
    production : {
      user : "ubuntu",
      host : "54.93.172.29",
      ref  : "origin/master",
      repo : "git@github.com:Dalas/course-project.git",
      path : "/srv/course-project"
    }
  }
};
