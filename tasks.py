from invoke import task

@task
def test(c):
    c.run('coverage run -m unittest discover')

@task(test)
def cov(c):
    c.run('coverage html')
    c.run('coverage report')

@task
def sync(c):
    c.run('git fetch upstream')
    c.run('git merge upstream/master')
