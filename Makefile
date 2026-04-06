.PHONY: install harvest insights summarise all clean

install:
	uv sync

harvest:
	uv run bd-harvest --out-dir .

insights:
	uv run bd-insights --out-dir .

summarise:
	uv run bd-summarise --out-dir .

all:
	uv run bd-docs --out-dir .

clean:
	rm -rf bd/commands bd/insights bd/summary
