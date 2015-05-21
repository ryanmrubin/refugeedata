var gulp = require('gulp');
var sass = require('gulp-sass');
var shell = require('gulp-shell');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var gzip = require('gulp-gzip');
var livereload = require('gulp-livereload');

var gzip_options = {
    threshold: '1kb',
    gzipOptions: {
        level: 9
    }
};

/* Compile Our Sass */
gulp.task('sass', function() {
    return gulp.src('scss/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('refugeedata/static/css'))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest('refugeedata/static/css'))
        .pipe(gzip(gzip_options))
        .pipe(gulp.dest('refugeedata/static/css'))
        .pipe(livereload());
});

/* Watch Files For Changes */
gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('scss/*.scss', ['sass']);

    /* Trigger a live reload on any Django template changes */
    gulp.watch('**/templates/*').on('change', livereload.changed);

});

gulp.task('django', shell.task(['. $VIRTUAL_ENV/bin/activate && python ./manage.py runserver 0.0.0.0:8000']));

gulp.task('default', ['sass', 'django', 'watch']);
