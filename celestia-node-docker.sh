#!/usr/bin/env sh
NETWORK=celestia
NODE_TYPE=light
RPC_URL=rpc.celestia.pops.one
docker run -e NODE_TYPE=$NODE_TYPE -e P2P_NETWORK=$NETWORK \
    -v ./node-data:/home/celestia \
    ghcr.io/celestiaorg/celestia-node:v0.20.2 \
    celestia $NODE_TYPE start --core.ip $RPC_URL --p2p.network $NETWORK
