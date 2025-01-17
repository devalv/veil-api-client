# -*- coding: utf-8 -*-
"""Concrete VeiL api objects."""
from .cluster import VeilCluster
from .controller import VeilController
from .data_pool import VeilDataPool
from .domain import (DomainBackupConfiguration, DomainConfiguration, DomainTcpUsb,
                     DomainUpdateConfiguration, VeilDomain, VeilGuestAgentCmd)
from .library import VeilLibrary
from .node import VeilNode
from .resource_pool import VeilResourcePool
from .vdisk import VeilVDisk
from ..base import VeilRestPaginator


class VeilDomainExt(VeilDomain):
    """Extension of VeilDomain with methods related to VeilLibrary."""

    async def backup_list(self, paginator: VeilRestPaginator = None):
        """List of domain backup files."""
        lib = VeilLibrary(client=self._client,
                          retry_opts=self.retry_opts,
                          cache_opts=self.cache_opts)
        return await lib.list(domain=self.api_object_id,
                              paginator=paginator)


__all__ = (
    'DomainConfiguration', 'VeilGuestAgentCmd', 'DomainTcpUsb', 'VeilDomainExt',
    'DomainBackupConfiguration', 'VeilLibrary', 'VeilNode', 'VeilController',
    'VeilDataPool', 'VeilResourcePool', 'VeilVDisk', 'VeilCluster',
    'DomainUpdateConfiguration'
)
