TAG_NAME := DEPLOY
TAG_DATE := $(TAG_NAME)_$(shell date -u "+%Y_%m_%d_%H_%M_%S")


deploy:
	npm run build
	scp -r dist/* guiguide@ssh-guiguide.alwaysdata.net:/home/guiguide/www/cero_vs_ebird/
	git tag $(TAG_DATE); git push origin $(TAG_DATE) --no-verify

processSpecies:
	npm run processSpecies

dev:
	npm run dev
