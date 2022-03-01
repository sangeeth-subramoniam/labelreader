//読み込み中を表示するjs
(function($) {
	/**
	 * インジケータ表示範囲を管理するコントローラ
	 *
	 * @class indicatorController
	 */

	var indicatorController = {

		__name: 'indicatorAllController',

		/**
		 * インジケータ表示ボタン押下イベント
		 *
		 * @memberOf indicatorController
		 */


		'#indicator click': function(){

			//インジケータ表示
			this.indicator({
				message: '読み込み中...',
				target : document.body
			}).show();
		}
	};
	$(function(){
		h5.core.controller('#indicator-target', indicatorController);
	})
})(jQuery);