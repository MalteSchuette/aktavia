export interface Case {
    id: number;
    reference: string;
    client: string;
    opponent: string;
    area_of_law: string;
    responsible_lawyer: number;
    responsible_lawyer_name: string;
    status: "active" | "dormant" | "closed";
    created_at: string;
    updated_at: string;
}