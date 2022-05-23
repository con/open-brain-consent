LOGO_SVG=OBC_LogoCheck.svg

all: OBC_LogoCheck.pdf OBC_LogoCheck.png favicon.png

favicon.png: $(LOGO_SVG)
	@inkscape "$<" -o "$@" --export-height 32

%.png: %.svg
	@echo "Rendering $@"
	@inkscape "$<" -o "$@" -d 150

%.pdf: %.svg
	@echo "Rendering $@"
	@inkscape "$<" -o "$@"

