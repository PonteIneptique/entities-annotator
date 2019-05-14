from annotator.app import app, db
from annotator.models import Word, Mention
from flask import render_template, request


@app.route("/")
def index():
    return render_template(
        "main/index.html",
        words=Word.query.paginate(
            page=int(request.args.get("page", 1)),
            per_page=50
        )
    )


@app.route("/word/<int:word_id>", methods=("POST", "GET"))
def word(word_id):
    word = Word.query.get_or_404(word_id)
    if request.method == "POST":
        word.categories = request.form.get("category", None)
    db.session.add(word)
    db.session.commit()
    return render_template(
        "main/word.html",
        word=word
    )

