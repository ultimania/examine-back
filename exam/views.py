from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from django.db.models import Q
from django.urls import reverse_lazy

# Create your views here.
class BaseView(generic.edit.FormView):
    """各ビュークラスの基底クラス
    """

    namespace = None
    model = ExamTr
    context_object_name = 'context'
    template_name = None
    paginate_by = None
    login_url = None
    redirect_field_name = None
    form_class = None
    exam = None

    def get_success_url(self):
        """reverse()で試験ID（self.object.id）をパラメータに遷移先画面を呼び出す

        Args:
            None

        Returns:
            none
        
        Examples:
            None
        """
        return reverse('exam:config', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.namespace
        context['namespace'] = self.namespace
        return context


class ConfigView(BaseView, generic.edit.CreateView):
    """各ビュークラスの基底クラス
    """

    namespace = 'config'
    template_name = 'exam/config.html'
    form_class = ConfigForm


class ExamView(BaseView, generic.edit.UpdateView):
    """各ビュークラスの基底クラス
    """

    namespace = 'exam'
    template_name = 'exam.html'
    form_class = ExamForm


class ResultView(BaseView, generic.edit.UpdateView):
    """各ビュークラスの基底クラス
    """

    namespace = 'result'
    template_name = 'result.html'
    form_class = ResultForm


class ReportView(BaseView, generic.edit.CreateView):
    """各ビュークラスの基底クラス
    """

    namespace = 'report'
    template_name = 'report.html'
    form_class = ReportForm
