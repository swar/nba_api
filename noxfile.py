import nox


@nox.session(python="3.6")
def test(session):
    # Install requirements
    session.install("-r", "requirements.txt")
    session.install("-e", ".")
    # Pytest
    session.install("pytest")
    session.run("pytest", "-k", "not slow")
