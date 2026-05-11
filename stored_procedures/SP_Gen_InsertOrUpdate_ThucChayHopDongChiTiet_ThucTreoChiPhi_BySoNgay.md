# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreoChiPhi_BySoNgay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-06-17 09:27:13.133000
- **Ngày sửa cuối**: 2019-06-17 09:28:23.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoNgay` | `int(4)` | No |

## Definition (Source Code)

```sql

/*ThucChayHopDongChiTiet_ThucTreoChiPhi
EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreoChiPhi_BySoNgay] @SoNgay = 3
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreoChiPhi_BySoNgay]
	@SoNgay INT
AS
BEGIN
    DECLARE @NgayThucHien DATETIME;
    DECLARE @SQL NVARCHAR(MAX),
            @LoaiThucTreo_chiphi NVARCHAR(50) = N'ChiPhi';
    SET @NgayThucHien = ISNULL(
                        (
                            SELECT MAX(dchdct.LastModifiedAt)
                            FROM dbo.ThucChayHopDongChiTiet dchdct
                            WHERE dchdct.LoaiThucTreo = @LoaiThucTreo_chiphi
                        ),
                        '1900-01-01'
                              );

    SET @NgayThucHien = DATEADD(DAY, -@SoNgay, @NgayThucHien);
    --SET @NgayThucHien = '2009-01-01'

    PRINT @NgayThucHien;
    CREATE TABLE #ThucChayHopDongChiTiet
    (
        [ThucChayHopDongChiTietID] [INT] NOT NULL,
        [HopDongREF] [INT] NULL,
        [NhanHang] [NVARCHAR](500) NULL,
        [ThoiGianBatDau] [DATETIME] NULL,
        [ThoiGianKetThuc] [DATETIME] NULL,
        [Link] [NVARCHAR](2000) NULL,
        [DmBannerREF] [NVARCHAR](255) NULL,
        [TenBanner] [NVARCHAR](255) NULL,
        [ViTri] [NVARCHAR](255) NULL,
        [GhiChu] [NVARCHAR](2555) NULL,
        [BookingREF] [INT] NULL,
        [HopDongChiTietREF] [INT] NULL,
        [TypeThucChay] [INT] NULL,
        [CreatedBy] [NVARCHAR](50) NULL,
        [CreatedAt] [DATETIME] NOT NULL,
        [LastModifiedBy] [NVARCHAR](50) NULL,
        [LastModifiedAt] [DATETIME] NOT NULL,
        [DeletedStatus] [INT] NOT NULL,
        [PrintStatus] [INT] NOT NULL,
        [RecordStatus] [INT] NOT NULL,
        [DmViTriREF] [INT] NULL,
        [DmNhanHangREF] [NVARCHAR](200) NULL,
        [SoLuongThucTreo] [FLOAT] NULL,
        [SoLuongThucChay] [FLOAT] NULL,
        [DmDonViTinhREF] [BIGINT] NULL,
        [DonViTinh] [NVARCHAR](200) NULL,
        [DmHinhThucQuangCaoREF] [INT] NULL,
        [TenHinhThucQuangCao] [NVARCHAR](200) NULL,
        [DmSanPhamREF] [INT] NULL,
        [TenSanPham] [NVARCHAR](200) NULL,
        [InputType] [INT] NULL,
        [IsReadBooking] [INT] NULL,
        [KichThuoc] [NVARCHAR](200) NULL,
        [DonGia] FLOAT NULL,
        [ChietKhau] FLOAT NULL,
        [ThanhTien] FLOAT NULL,
        [LoaiThucTreo] NVARCHAR(50),
        [STATUS] SMALLINT
    );

    INSERT INTO #ThucChayHopDongChiTiet
    (
        ThucChayHopDongChiTietID,
        HopDongREF,
        NhanHang,
        ThoiGianBatDau,
        ThoiGianKetThuc,
        Link,
        DmBannerREF,
        TenBanner,
        ViTri,
        GhiChu,
        BookingREF,
        HopDongChiTietREF,
        TypeThucChay,
        CreatedBy,
        CreatedAt,
        LastModifiedBy,
        LastModifiedAt,
        DeletedStatus,
        PrintStatus,
        RecordStatus,
        DmViTriREF,
        DmNhanHangREF,
        SoLuongThucTreo,
        SoLuongThucChay,
        DmDonViTinhREF,
        DonViTinh,
        DmHinhThucQuangCaoREF,
        TenHinhThucQuangCao,
        DmSanPhamREF,
        TenSanPham,
        InputType,
        IsReadBooking,
        KichThuoc,
        DonGia,
        ChietKhau,
        ThanhTien,
        LoaiThucTreo,
        STATUS
    )
    SELECT tt.ThucTreoHopDongChiTietTrinhDuyetID,
           tt.HopDongREF,
           tt.TenNhanHang,
           ISNULL(tt.NgayBatDau,'2010-01-01') AS NgayBatDau,
           tt.NgayKetThuc,
           tt.Linkbai,
           0 AS DmBannerREF,
           '' AS TenBanner,
           '' AS ViTri,
           tt.Note,
           0 AS BookingREF,
           tt.HopDongChiTietREF,
           0 AS TypeThucChay,
           tt.CreatedBy,
           tt.CreatedAt,
           tt.LastModifiedBy,
           tt.LastModifiedAt,
           tt.DeletedStatus,
           0 AS Print_Status,
           0 AS Record_Status,
           0 AS DmViTriREF,
           tt.NhanHangREF,
           tt.Soluong,
           tt.Soluong,
           tt.DmDonViTinhREF,
           tt.DonViTinh,
           tt.DmHinhThucQuangCaoREF,
           ISNULL(
           (
               SELECT TOP (1)
                      TenHinhThucQuangCao
               FROM dbo.DmHinhThucQuangCao
               WHERE DmHinhThucQuangCaoID = tt.DmHinhThucQuangCaoREF
               ORDER BY DmHinhThucQuangCaoID
           ),
           ''
                 ) AS TenHinhThucQuangCao,
           tt.DmSanPhamREF,
           ISNULL(
           (
               SELECT TOP (1)
                      TenSanPham
               FROM dbo.DmSanPham
               WHERE DmSanPhamID = tt.DmSanPhamREF
               ORDER BY DmSanPhamID
           ),
           ''
                 ) AS TenSanPham,
           0 AS InputType,
           0 AS IsReadBooking,
           '' AS KichThuoc,
           tt.DonGia,
           tt.ChietKhau,
           tt.TongTien,
           @LoaiThucTreo_chiphi AS LoaiThucTreo,
           0 AS status_table
    FROM dbo.ThucTreoHopDongChiTietTrinhDuyet_ThucTreo tt
    WHERE tt.LastModifiedAt >= @NgayThucHien
	and TrangThai = 2;

	

    UPDATE #ThucChayHopDongChiTiet
    SET [STATUS] = 1
    FROM #ThucChayHopDongChiTiet t
        INNER JOIN dbo.ThucChayHopDongChiTiet dc
            ON t.ThucChayHopDongChiTietID = dc.ThucChayHopDongChiTietID
    --WHERE dc.LoaiThucTreo = @LoaiThucTreo_chiphi;

    -- Update nhung row da ton ton                                      
    UPDATE [dbo].[ThucChayHopDongChiTiet]
    SET [HopDongREF] = A.HopDongREF,
        [HopDongChiTietREF] = A.HopDongChiTietREF,
        [DmBannerREF] = A.DmBannerREF,
        [TenBanner] = A.TenBanner,
        [DmViTriREF] = A.DmViTriREF,
        [ViTri] = A.ViTri,
        [DmNhanHangREF] = A.DmNhanHangREF,
        [NhanHang] = [dbo].[ReplaceNhanHangDoubleNhay](A.NhanHang),
        [BookingREF] = A.BookingREF,
        [ThoiGianBatDau] = A.ThoiGianBatDau,
        [ThoiGianKetThuc] = A.ThoiGianKetThuc,
        [SoLuongThucTreo] = A.SoLuongThucTreo,
        [SoLuongThucChay] = A.SoLuongThucChay,
        [DmDonViTinhREF] = A.DmDonViTinhREF,
        [DonViTinh] = A.DonViTinh,
        [TypeThucChay] = A.TypeThucChay,
        [Link] = A.Link,
        [GhiChu] = A.GhiChu,
        [DmHinhThucQuangCaoREF] = A.DmHinhThucQuangCaoREF,
        [TenHinhThucQuangCao] = A.TenHinhThucQuangCao,
        [DmSanPhamREF] = A.DmSanPhamREF,
        [TenSanPham] = A.TenSanPham,
        [InputType] = A.InputType,
        [IsReadBooking] = A.IsReadBooking,
		DeletedStatus = A.DeletedStatus,
        [CreatedBy] = A.CreatedBy,
        [CreatedAt] = A.CreatedAt,
        [LastModifiedBy] = A.LastModifiedBy,
        [LastModifiedAt] = A.LastModifiedAt,
        [KichThuoc] = A.KichThuoc,
        [DonGia] = A.DonGia,
        [ChietKhau] = A.ChietKhau,
        [ThanhTien] = A.ThanhTien
    FROM #ThucChayHopDongChiTiet A
    WHERE [STATUS] = 1
          AND A.ThucChayHopDongChiTietID = ThucChayHopDongChiTiet.ThucChayHopDongChiTietID
          --AND ThucChayHopDongChiTiet.LoaiThucTreo = @LoaiThucTreo_chiphi;

    -- Insert Row chua ton tai
    INSERT INTO [dbo].[ThucChayHopDongChiTiet]
    (
        [ThucChayHopDongChiTietID],
        [HopDongREF],
        [HopDongChiTietREF],
        [DmBannerREF],
        [TenBanner],
        [DmViTriREF],
        [ViTri],
        [DmNhanHangREF],
        [NhanHang],
        [BookingREF],
        [ThoiGianBatDau],
        [ThoiGianKetThuc],
        [SoLuongThucTreo],
        [SoLuongThucChay],
        [DmDonViTinhREF],
        [DonViTinh],
        [TypeThucChay],
        [Link],
        [GhiChu],
        [DmHinhThucQuangCaoREF],
        [TenHinhThucQuangCao],
        [DmSanPhamREF],
        [TenSanPham],
        [InputType],
        [IsReadBooking],
        [CreatedBy],
        [CreatedAt],
        [LastModifiedBy],
        [LastModifiedAt],
        [DeletedStatus],
        [PrintStatus],
        [RecordStatus],
        [KichThuoc],
        [DonGia],
        [ChietKhau],
        [ThanhTien],
        [LoaiThucTreo]
    )
    SELECT [ThucChayHopDongChiTietID],
           [HopDongREF],
           [HopDongChiTietREF],
           [DmBannerREF],
           [TenBanner],
           [DmViTriREF],
           [ViTri],
           [DmNhanHangREF],
           [dbo].[ReplaceNhanHangDoubleNhay]([NhanHang]),
           [BookingREF],
           [ThoiGianBatDau],
           [ThoiGianKetThuc],
           [SoLuongThucTreo],
           [SoLuongThucChay],
           [DmDonViTinhREF],
           [DonViTinh],
           [TypeThucChay],
           [Link],
           [GhiChu],
           [DmHinhThucQuangCaoREF],
           [TenHinhThucQuangCao],
           [DmSanPhamREF],
           [TenSanPham],
           [InputType],
           [IsReadBooking],
           [CreatedBy],
           [CreatedAt],
           [LastModifiedBy],
           [LastModifiedAt],
           [DeletedStatus],
           [PrintStatus],
           [RecordStatus],
           [KichThuoc],
           [DonGia],
           [ChietKhau],
           [ThanhTien],
           @LoaiThucTreo_chiphi
    FROM #ThucChayHopDongChiTiet dchdct
    WHERE dchdct.[STATUS] = 0;

    DROP TABLE #ThucChayHopDongChiTiet;

END;


```
