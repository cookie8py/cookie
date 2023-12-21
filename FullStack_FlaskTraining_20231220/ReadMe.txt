이 사례에서 강사는 훨씬 더 큰 애플리케이션을 구축하고 있습니다.

'정적' 폴더와 '템플릿' 폴더가 들어 있는 '애플리케이션' 폴더가 있습니다. 이 폴더가 전체 프로젝트의 모듈이 됩니다.

정적 폴더 안에는 CSS와 이미지라는 두 개의 폴더가 있습니다.

템플릿 폴더 안에는 '포함' 폴더가 있습니다. 여기에는 바닥글 및 탐색과 같은 HTML 조각이 들어 있습니다. 이 폴더는 다른 템플릿에서 사용되며 다른 템플릿으로 가져올 때 Jinjja를 사용합니다.

index.html 템플릿에는 하나의 조건문이 있으며 전달된 변수를 사용하여 서로 다른 두 줄의 html을 표시합니다.

main.py는 이제 아주 최소한으로 줄었습니다. 애플리케이션 모듈(애플리케이션 폴더의 파일)만 가져옵니다.

config.py는 "비밀 키"를 가지고 있으며 os 모듈을 가져옵니다.

__init__.py는 애플리케이션이 실제로 시작되는 곳이며 나머지 애플리케이션에 대한 참조를 포함합니다. 이것은 또한 routes.py를 가져옵니다.

routes.py에는 사용된 모든 경로가 포함되어 있습니다. 여기서 Flask에 대한 import 문에는 render_template만 필요합니다.


In this couse, the instructor is building a much larger application.

There is an "application" folder which contains the 'static' and 'templates' folders. This will be the module for the entire project.

Inside the static folder, there are two folders: css and images

Inside the templates folder, there is an 'includes' folder. This contains html pieces such as the footer and the navigation. These will be used across the other templates and use Jinjja to import into the other templates.

The index.html template has one conditional statement and uses the passed variable to show two different lines of html.

main.py is very minimal now. It only imports the application module (the files from the application folder.)

config.py has the "secret key" and imports the os module.

__init__.py is where the application actually starts and contains references to the rest of the application. This also imports routes.py

routes.py contains all the routes used. The import statement for Flask here only requires the render_template.

