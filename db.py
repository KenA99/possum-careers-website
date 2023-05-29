from sqlalchemy import create_engine, text


engine = create_engine(
"mysql+pymysql://p8xutv8csrb78sow73qv:pscale_pw_lgStydD5WWtBxEkc4oLnBq4dS12yfhZd66O1AwlalVa@aws.connect.psdb.cloud",
  connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}
    )

def load_jobs():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    jobs = []
    for row in result.all():
      jobs.append(row)
    return jobs
