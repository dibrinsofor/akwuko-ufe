from flask import Flask
from flask.signals import message_flashed
from flask_restful import Api, Resource, abort, reqparse, marshal_with, fields, inputs
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# .strftime("%B %d %Y ")


class StoryModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    field = db.Column(db.String(20), nullable=False)
    cover_img = db.Column(db.String, nullable=False)
    audio_url = db.Column(db.String, nullable=False)
    summary = db.Column(db.String, nullable=True)
    addi_img = db.Column(db.String, nullable=True)
    date = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "story(id={id}, title={title}, posted on={date}, with content={content}, likes={likes}, field={field}, cover_img={cover_img}, audio_url={audio_url}, summary={summary}, addi_img={addi_img})"

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("title", type=str, help="Title of story needed", required= True)
video_put_args.add_argument("content", type=str, help="Story needed", required = True)
video_put_args.add_argument("likes", type=int, help="number of likes not passed", required = True)
video_put_args.add_argument("field", type=str, help="field of story needed", required = True)
video_put_args.add_argument("date", type=inputs.date, help="Date of Story - YYYY-mm-dd", required = True)
video_put_args.add_argument("cover_img", type=inputs.url, help="url of header image needed", required = True)
video_put_args.add_argument("audio_url", type=inputs.url, help="url of story audio needed", required = True)
video_put_args.add_argument("summary", type=str, help="aim of story can be added")
video_put_args.add_argument("addi_img", type=inputs.url, help="additional story images can be added")
# compare if we dont like the format of the date from falsk restful parser.add_argument('date', type=lambda x: datetime.strptime(x,'%Y-%m-%dT%H:%M:%S'))

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("title", type=str, help="Title of the story needed")
video_update_args.add_argument("content", type=str, help="Story needed")
video_update_args.add_argument("likes", type=int, help="Number of likes not passed")
video_update_args.add_argument("field", type=str, help="field of story needed")
video_update_args.add_argument("date", type=inputs.date, help="Date of Story - YYYY-mm-dd")
video_update_args.add_argument("cover_img", type=inputs.url, help="url of header image")
video_update_args.add_argument("audio_url", type=inputs.url, help="url of story audio")
video_update_args.add_argument("summary", type=str, help="aim of story")
video_update_args.add_argument("addi_img", type=inputs.url, help="additional story images")

resource_fields = {
    'id': fields.Integer, 
    'title': fields.String, 
    'content': fields.String, 
    'likes': fields.Integer, 
    'field': fields.String, 
    'date': fields.String,
    'cover_img': fields.String, 
    'audio_url': fields.String, 
    'summary': fields.String, 
    'addi_img': fields.String
}

# db.create_all()

class Story(Resource):
    @marshal_with(resource_fields)
    def get(self, story_id=None):
        if story_id is None:
            result = StoryModel.query.all()
            return result
        else: 
            result = StoryModel.query.filter_by(id=story_id).first()
            return result

    @marshal_with(resource_fields)
    def put(self, story_id):
        args = video_put_args.parse_args()
        result = StoryModel.query.filter_by(id=story_id).first()
        if result:
            abort(409, message_flashed="Video already exists")
        story = StoryModel(id=story_id, title=args['title'], 
                            content=args['content'], likes=args['likes'], 
                            field=args['field'], cover_img=args['cover_img'], 
                            audio_url=args['audio_url'], summary=args['summary'], 
                            addi_img=args['addi_img'], date=args['date'])
        db.session.add(story)
        db.session.commit()
        return story, 201

    def delete(self, story_id):
        StoryModel.query.filter_by(id=story_id).delete()
        db.session.commit()
        return f"Deleted {story_id}", 204

    @marshal_with(resource_fields)
    def patch(self, story_id):
        args = video_update_args.parse_args()
        result = StoryModel.query.filter_by(id=story_id).first()
        if not result:
            abort(404, message_flashed="Video does not exist")
        
        if args['title']:
            result.title = args["title"]
        if args['content']:
            result.content = args["content"]
        if args['likes']:
            result.likes = args["likes"]
        if args['field']:
            result.field = args['field']
        if args['cover_img']:
            result.field = args['cover_img']
        if args['audio_url']:
            result.field = args['audio_url']
        if args['summary']:
            result.field = args['summary']     
        if args['addi_img']:
            result.field = args['addi_img']       

        # db.session.add(result)
        db.session.commit()

        return result


api.add_resource(Story, 
                        "/api/story/<int:story_id>", 
                        "/story/", 
                        "/story/<int:story_id>",
                        "/api/story/")

if __name__ == "__main__":
    app.run(debug=True)