from flask import Flask, request
# JWT 사용을 위한 SECRET_KEY 정보가 들어있는 파일 임포트
from config import Config
from flask.json import jsonify
from http import HTTPStatus

from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.follow import FollowListResource, FollowResource, SearchUserResource


from resources.posting import PostingResource,PostingeditResource,delPostingResource
from resources.postinglist import myPostinginfoResource ,allPostinginfoResource
from resources.user import UserInfoResource,UserLoginResource, UserLogoutResource, UserRegisterResource, jwt_blacklist
from resources.comment import commentResource,editcommentResource,delcommentResource


app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(Config)

# JWT 토큰 만들기
jwt = JWTManager(app)

# todo : 로그아웃 개발하고 나서, 코멘트 해제한다.
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload) :
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

api = Api(app)

# 경로와 리소스를 연결한다.
api.add_resource(UserRegisterResource, '/api/v1/user/register') # 회원가입
api.add_resource(UserLoginResource, '/api/v1/user/login') # 로그인
api.add_resource(UserLogoutResource, '/api/v1/user/logout') # 로그아웃 
api.add_resource(UserInfoResource, '/api/v1/user/info') # 내 정보 가져오기  
api.add_resource(PostingResource,'/api/v1/posting') # 업로드 하기 
api.add_resource(PostingeditResource,'/api/v1/editposting/<int:posting_id>') # 포스팅 수정 
api.add_resource(myPostinginfoResource,'/api/v1/mypostinginfo') # 내가 쓴 포스팅 정보가져오기
api.add_resource(allPostinginfoResource,'/api/v1/postinginfo') # 모든 포스팅 가져오기 
api.add_resource(delPostingResource,'/api/v1/deleteposting/<int:posting_id>') # 포스팅 삭제하기 
api.add_resource(FollowResource,'/api/v1/user/following/<int:f_user_id>') # 팔로우 추가/삭제
api.add_resource(FollowListResource,'/api/v1/user/following' ) # 팔로우 리스트
api.add_resource(SearchUserResource, '/api/v1/user/search') # 유저 검색
api.add_resource(commentResource,'/api/v1/comment/<int:posting_id>') # 댓글달기
api.add_resource(editcommentResource,'/api/v1/editcomment/<int:posting_id>/<int:comment_id>') # 댓글 수정 
api.add_resource(delcommentResource,'/api/v1/delcomment/<int:posting_id>/<int:comment_id>') # 댓글 삭제 

if __name__ == '__main__' :
    app.run()
