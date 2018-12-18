#!/usr/bin/python
# -*- coding: utf-8 -*-

# © Copyright 2018 CERN
#
# This software is distributed under the terms of the GNU Lesser General Public
# Licence version 3 (LGPL Version 3), copied verbatim in the file “LICENSE”
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

from .client import RunRegistryClient
from .utils import build_where_clause, list_to_dict


class RunInfo:
    def __init__(self):
        self.runregistry = RunRegistryClient()
        self.namespace = "runinfo"

    def get_runs(
        self,
        run_number=None,
        run_number_from=None,
        run_number_to=None,
        run_number_in=None,
    ):
        query = (
            "select "
            "min(r.RUNNUMBER) as RUN_NUMBER, "
            "min(r.LHCFILL) as LHC_FILL, "
            "max(r.LUMISECTION) as LUMISECTIONS, "
            "sum(r.DELIVLUMISECTION) as RUM_LUMI, "
            "sum(r.LIVELUMISECTION) as RUN_LIVE_LUMI "
            "from runinfo.lumi_sections r where {run_where} ".format(
                run_where=build_where_clause(
                    "r.runnumber",
                    run_number,
                    run_number_from,
                    run_number_to,
                    run_number_in,
                )
            )
            + "and r.CMS_ACTIVE = 1 group by r.runnumber"
        )

        response = self.runregistry.execute_query(query)
        keys = ["run_number", "lhc_fill", "lumisections", "run_lumi", "run_live_lumi"]
        return list_to_dict(response.get("data", None), keys)

    def get_run(self, run_number):
        try:
            return self.get_runs(run_number=run_number)[0]
        except IndexError:
            return None
