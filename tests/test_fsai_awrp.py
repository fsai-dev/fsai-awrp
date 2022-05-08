from fsai_awrp.fsai_awrp import ArgoWorkflowsReportProgress


def test_app():
    awrp = ArgoWorkflowsReportProgress()
    awrp.set_total_progress(100)
    awrp.set_current_progress(20)
    # awrp.start_reporting()
    assert True == True
