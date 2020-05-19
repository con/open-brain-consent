#!/bin/bash
#emacs: -*- mode: shell-script; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- 
#ex: set sts=4 ts=4 sw=4 noet:
#
#
# COPYRIGHT: Yaroslav Halchenko 2020
#
# LICENSE: MIT
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#

set -eu

ver_marker="\*\*Version:\*\* "

# first argument version; the rest are filenames
version=$1
shift

for f in "$@"; do
	# First inject the marker if not present at all
	grep -q -e "$ver_marker" "$f" || sed -e "s,\(-----------\)$,\1\n\n$ver_marker ,g" -i "$f"
	# Now replace existing version with desired value but also adding the language
	# if that one was defined in the $version provided
	lang=$(echo "$f" | sed -ne '/i18n/s,.*\.\([a-z][-a-z]*\)\.rst,\1,gp')
	version_lang=$(eval echo "$version")
	sed -i -e "s/$ver_marker.*/$ver_marker$version_lang/g" "$f"
done
