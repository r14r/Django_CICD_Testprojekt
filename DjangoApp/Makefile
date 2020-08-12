PREFIX_PKG := django_tutorial_polls


default:
	grep -E ':\s+#' Makefile

clearcache:
	python manage.py clearcache

run:
	python manage.py runserver 8000

deploy:
	rm -rf dist $(PREFIX_PKG)*
	rm -rf polls.dist
	cd polls && python setup.py sdist
	mkdir polls.dist && mv polls/dist/* polls/$(PREFIX_PKG)* polls.dist

install_bootstrap:
	cd .. && yarn add bootstrap
	rm -rf  polls/static/bootstrap
	mkdir   polls/static/bootstrap
	cp -R ../node_modules/bootstrap/dist/* polls/static/bootstrap

install_jquery:
	cd .. && yarn add jquery
	rm -rf polls/static/jquery
	mkdir  polls/static/jquery
	cp ../node_modules/jquery/dist/* polls/static/jquery

install_bootstrap_from_source:
	mkdir -p install && \
	wget https://github.com/twbs/bootstrap/releases/download/v4.1.3/bootstrap-4.1.3-dist.zip -O install/bootstrap-4.1.3-dist.zip && \
	unzip install/bootstrap-4.1.3-dist.zip -d polls/static/bootstrap/4.1.3
